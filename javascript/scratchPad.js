'use client'
// Cemetery checkout screen
import { useState, useEffect } from 'react'
import Image from 'next/image'
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { AspectRatio } from "@/components/ui/aspect-ratio"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

const products = [
  { id: 'plot-a', name: 'Plot Type A', price: 10000, quantity: 0 },
  { id: 'plot-b', name: 'Plot Type B', price: 15000, quantity: 0 },
  { id: 'plot-c', name: 'Plot Type C', price: 20000, quantity: 0 },
  { id: 'plot-d', name: 'Plot Type D', price: 35000, quantity: 0 },
]

const additionalServices = [
  { id: '2nd-burial', name: '2nd Burial', price: 0, quantity: 0, requiresPlotNumber: true },
  { id: '3rd-burial', name: '3rd Burial', price: 0, quantity: 0, requiresPlotNumber: true },
  { id: 'cremation', name: 'Cremation', price: 9000, quantity: 0, requiresPlotNumber: false },
  { id: 'exhumation', name: 'Exhumation', price: 3000, quantity: 0, requiresPlotNumber: true },
]

export default function CemeteryCheckout() {
  const [productQuantities, setProductQuantities] = useState(
    Object.fromEntries(products.map(p => [p.id, 0]))
  )
  const [serviceQuantities, setServiceQuantities] = useState(
    Object.fromEntries(additionalServices.map(s => [s.id, 0]))
  )
  const [plotNumbers, setPlotNumbers] = useState(
    Object.fromEntries(additionalServices.filter(s => s.requiresPlotNumber).map(s => [s.id, '']))
  )
  const [additionalPlotNumber, setAdditionalPlotNumber] = useState('');
  const [chapelHours, setChapelHours] = useState(0)
  const [userDetails, setUserDetails] = useState({
    name: '',
    email: '',
    phone: '',
  })
  const [familyMembers, setFamilyMembers] = useState([
    { name: '', relation: '' },
    { name: '', relation: '' },
    { name: '', relation: '' },
  ])
  const [paymentMethod, setPaymentMethod] = useState('online')
  const [promoCode, setPromoCode] = useState('')

  const calculateTotal = () => {
    const plotTotal = products.reduce((sum, product) => 
      sum + product.price * productQuantities[product.id], 0
    )
    const servicesTotal = additionalServices.reduce((sum, service) => 
      sum + service.price * serviceQuantities[service.id], 0
    )
    const chapelTotal = chapelHours * 400

    return plotTotal + servicesTotal + chapelTotal
  }

  const handleUserDetailsChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target
    setUserDetails(prev => ({ ...prev, [name]: value }))
  }

  const handleFamilyMemberChange = (index: number, field: string, value: string) => {
    setFamilyMembers(prev => 
      prev.map((member, i) => 
        i === index ? { ...member, [field]: value } : member
      )
    )
  }

  const addFamilyMember = () => {
    setFamilyMembers(prev => [...prev, { name: '', relation: '' }])
  }

  const handlePlotNumberChange = (serviceId: string, value: string) => {
    setPlotNumbers(prev => ({ ...prev, [serviceId]: value }))
  }

  const handleAdditionalPlotNumberChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setAdditionalPlotNumber(e.target.value);
  };

  return (
    <Card className="w-full max-w-3xl mx-auto">
      <CardHeader>
        <CardTitle>Cemetery Plot Checkout</CardTitle>
      </CardHeader>
      <CardContent className="space-y-6">
        <AspectRatio ratio={16 / 9} className="bg-muted">
          <Image
            src="/placeholder.svg?height=720&width=1280"
            alt="Cemetery Map"
            fill
            className="rounded-md object-cover"
          />
        </AspectRatio>

        <div>
          <h3 className="text-lg font-semibold mb-2">Select Plot Type</h3>
          {products.map((product) => (
            <div key={product.id} className="flex items-center space-x-2 mb-2">
              <Input
                type="number"
                min="0"
                value={productQuantities[product.id]}
                onChange={(e) => setProductQuantities(prev => ({
                  ...prev,
                  [product.id]: parseInt(e.target.value) || 0
                }))}
                className="w-20"
              />
              <Label htmlFor={product.id}>{product.name} - R{product.price}</Label>
            </div>
          ))}
        </div>

        <div>
          <h3 className="text-lg font-semibold mb-2">Additional Services</h3>
          {additionalServices.map((service) => (
            <div key={service.id} className="flex items-center space-x-2 mb-2">
              <Input
                type="number"
                min="0"
                value={serviceQuantities[service.id]}
                onChange={(e) => setServiceQuantities(prev => ({
                  ...prev,
                  [service.id]: parseInt(e.target.value) || 0
                }))}
                className="w-20"
              />
              <Label htmlFor={service.id}>
                {service.name}{service.price > 0 ? ` - R${service.price}` : ''}
              </Label>
              {service.requiresPlotNumber && serviceQuantities[service.id] > 0 && (
                <Input
                  placeholder="Plot Number"
                  value={plotNumbers[service.id]}
                  onChange={(e) => handlePlotNumberChange(service.id, e.target.value)}
                  className="w-32"
                />
              )}
            </div>
          ))}
        </div>

        {Object.values(serviceQuantities).some(quantity => quantity > 0) && (
          <div>
            <h3 className="text-lg font-semibold mb-2">Additional Plot Number</h3>
            <div className="flex items-center space-x-2 mb-2">
              <Input
                placeholder="Plot Number for Additional Services"
                value={additionalPlotNumber}
                onChange={handleAdditionalPlotNumberChange}
                className="w-full"
              />
            </div>
          </div>
        )}

        <div>
          <h3 className="text-lg font-semibold mb-2">Chapel Rental</h3>
          <div className="flex items-center space-x-2">
            <Input
              type="number"
              min="0"
              value={chapelHours}
              onChange={(e) => setChapelHours(parseInt(e.target.value) || 0)}
              className="w-20"
            />
            <Label>Hours (R400 per hour)</Label>
          </div>
        </div>

        <div>
          <h3 className="text-lg font-semibold mb-2">Your Details</h3>
          <div className="space-y-2">
            <div>
              <Label htmlFor="name">Full Name</Label>
              <Input
                id="name"
                name="name"
                value={userDetails.name}
                onChange={handleUserDetailsChange}
              />
            </div>
            <div>
              <Label htmlFor="email">Email</Label>
              <Input
                id="email"
                name="email"
                type="email"
                value={userDetails.email}
                onChange={handleUserDetailsChange}
              />
            </div>
            <div>
              <Label htmlFor="phone">Phone</Label>
              <Input
                id="phone"
                name="phone"
                type="tel"
                value={userDetails.phone}
                onChange={handleUserDetailsChange}
              />
            </div>
          </div>
        </div>

        <div>
          <h3 className="text-lg font-semibold mb-2">Family Members (Optional)</h3>
          {familyMembers.map((member, index) => (
            <div key={index} className="space-y-2 mb-4">
              <div>
                <Label htmlFor={`family-name-${index}`}>Name</Label>
                <Input
                  id={`family-name-${index}`}
                  value={member.name}
                  onChange={(e) => handleFamilyMemberChange(index, 'name', e.target.value)}
                />
              </div>
              <div>
                <Label htmlFor={`family-relation-${index}`}>Relation</Label>
                <Input
                  id={`family-relation-${index}`}
                  value={member.relation}
                  onChange={(e) => handleFamilyMemberChange(index, 'relation', e.target.value)}
                />
              </div>
            </div>
          ))}
          <Button type="button" onClick={addFamilyMember} className="mt-2">
            Add Family Member
          </Button>
        </div>

        <div>
          <h3 className="text-lg font-semibold mb-2">Payment Method</h3>
          <Select value={paymentMethod} onValueChange={setPaymentMethod}>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Select payment method" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="online">Online Payment</SelectItem>
              <SelectItem value="eft">EFT</SelectItem>
              <SelectItem value="cash">Cash</SelectItem>
            </SelectContent>
          </Select>
        </div>

        <div>
          <h3 className="text-lg font-semibold mb-2">Promo Code</h3>
          <div className="flex items-center space-x-2">
            <Input
              placeholder="Enter promo code"
              value={promoCode}
              onChange={(e) => setPromoCode(e.target.value)}
            />
            <Button type="button">Apply</Button>
          </div>
        </div>

        <div className="text-xl font-bold">
          Total: R{calculateTotal()}
        </div>
      </CardContent>
      <CardFooter>
        <Button className="w-full">Proceed to Checkout</Button>
      </CardFooter>
    </Card>
  )
}


