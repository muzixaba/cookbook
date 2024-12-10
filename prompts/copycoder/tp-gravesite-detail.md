Create detailed components with these requirements:
1. Use 'use client' directive for client-side components
2. Style with Tailwind CSS utility classes for responsive design
3. Use Lucide React for icons (from lucide-react package). Do NOT use other UI libraries unless requested
4. Use stock photos from picsum.photos where appropriate, only valid URLs you know exist
5. Configure next.config.js image remotePatterns to enable stock photos from picsum.photos
6. Avoid duplicate components
7. Automatically source and display logos from a CDN in design placeholders
8. Follow proper import practices:
   - Use @/ path aliases
   - Keep component imports organized
   - Update current src/app/page.tsx with new comprehensive code
   - Don't forget root route (page.tsx) handling
   - You MUST complete the entire prompt before stopping

Cemetery Management Mobile Interface
</summary_title>

<image_analysis>

1. Navigation Elements:
- Back button in header
- Edit buttons for key sections
- Open in Maps link for location


2. Layout Components:
- Profile header section (120px height)
- Information cards with 16px padding
- Grid layout for images (3x3)
- Map preview container (200px height)


3. Content Sections:
- Profile information
- Voucher code section
- Deceased person details
- Grave site information
- Contact list
- Image gallery
- Location map


4. Interactive Controls:
- Edit buttons with green accent
- Image upload placeholders
- Map interaction button
- Back navigation
- Profile image with add button


5. Colors:
- Primary Green: #4CAF50 (Edit buttons)
- Background: #FFFFFF
- Text: #000000
- Secondary Text: #666666
- Border: #EEEEEE


6. Grid/Layout Structure:
- Single column layout
- 16px horizontal margins
- Card-based content blocks
- 3x3 image grid with equal spacing
</image_analysis>

<development_planning>

1. Project Structure:
```
src/
├── components/
│   ├── layout/
│   │   ├── Header
│   │   └── InfoCard
│   ├── features/
│   │   ├── GraveDetails
│   │   ├── ContactList
│   │   └── ImageGallery
│   └── shared/
├── assets/
├── styles/
├── hooks/
└── utils/
```


2. Key Features:
- Grave site information management
- Contact information handling
- Image gallery with upload
- Location mapping integration
- Voucher code system


3. State Management:
```typescript
interface AppState {
├── gravesite: {
│   ├── details: GraveSiteDetails
│   ├── images: Image[]
│   ├── location: GeoCoordinates
├── }
├── contacts: {
│   ├── list: Contact[]
│   └── status: 'loading' | 'ready'
├── }
}
```


4. Routes:
```typescript
const routes = [
├── '/profile',
├── '/grave-details/*',
├── '/contacts/*',
└── '/location/*'
]
```


5. Component Architecture:
- ProfileHeader
- VoucherCode
- DeceasedInfo
- GraveSiteInfo
- ContactsList
- ImageGallery
- LocationMap


6. Responsive Breakpoints:
```scss
$breakpoints: (
├── mobile: 320px,
├── tablet: 768px,
├── desktop: 1024px,
└── wide: 1440px
);
```
</development_planning>