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

Cemetery Plot Management Dashboard Interface
</summary_title>

<image_analysis>

1. Navigation Elements:
- Top header bar with: Mt Hope, People, Plots, Map, Burials, Sales, Work Orders, Reports
- Search functionality in top-right
- User profile menu in far top-right


2. Layout Components:
- Full-width map interface (100vw)
- Plot grid overlay system
- Legend panel (positioned top-right)
- Map controls (positioned left side)
- Zoom controls (positioned bottom-right)


3. Content Sections:
- Interactive map as primary content
- Plot grid overlay showing:
  - Color-coded status indicators
  - Individual plot boundaries
  - Section identifiers
- Legend showing plot statuses:
  - Sold (red)
  - Occupied (pink)
  - Available (green)
  - Unavailable (white)


4. Interactive Controls:
- Zoom in/out buttons
- Pan navigation
- Plot selection capability
- Layer toggle controls
- Search functionality
- Section identifier markers


5. Colors:
- #FF0000 (Red) - Sold plots
- #FFC0CB (Pink) - Occupied plots
- #90EE90 (Light green) - Available plots
- #FFFFFF (White) - Unavailable plots
- #333333 (Dark gray) - Grid lines
- #FFFFFF (White) - Background


6. Grid/Layout Structure:
- Plot grid system with uniform sizing
- Organized in sections with clear boundaries
- Responsive scaling based on zoom level
- Consistent spacing between plot rows and columns
</image_analysis>

<development_planning>

1. Project Structure:
```
src/
├── components/
│   ├── layout/
│   │   ├── Header
│   │   ├── MapContainer
│   │   └── Legend
│   ├── features/
│   │   ├── PlotGrid
│   │   ├── MapControls
│   │   └── SearchBar
│   └── shared/
├── assets/
├── styles/
├── hooks/
└── utils/
```


2. Key Features:
- Interactive plot selection
- Real-time status updates
- Plot information display
- Search and filtering
- Export capabilities
- User permissions management


3. State Management:
```typescript
interface AppState {
├── plots: {
│   ├── selectedPlot: Plot
│   ├── plotStatus: Record<string, Status>
│   └── plotData: PlotData[]
├── }
├── map: {
│   ├── zoom: number
│   ├── center: Coordinates
│   └── bounds: Bounds
├── }
}
```


4. Routes:
```typescript
const routes = [
├── '/dashboard',
├── '/plots/*',
├── '/sales/*',
└── '/reports/*'
]
```


5. Component Architecture:
- MapContainer (parent)
├── PlotGrid (child)
├── MapControls (child)
├── Legend (child)
└── SearchOverlay (child)


6. Responsive Breakpoints:
```scss
$breakpoints: (
├── 'tablet': 768px,
├── 'desktop': 1024px,
├── 'large': 1440px,
└── 'xlarge': 1920px
);
```
</development_planning>