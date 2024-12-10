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

Cemetery Plot Management Dashboard
</summary_title>

<image_analysis>

1. Navigation Elements:
- Top navbar with: Mt Hope, People, Plots, Map, Burials, Sales, Work Orders, Tasks, Reports
- Left sidebar with: Entities menu containing A, B, D, Family Lots, Lawn, Mausoleum, New, New Section (Lower), VW, VW Section, Westside, XYZ


2. Layout Components:
- Header height: ~60px
- Left sidebar width: ~200px
- Main content area: flexible width
- Table row height: ~40px
- Padding: 16px between sections


3. Content Sections:
- Page title "All Plots"
- Description text
- Filter controls bar
- Data table with columns: checkbox, PLOT, OWNER, BURIALS
- Status badges: "Occupied", "Sold"


4. Interactive Controls:
- Search bar in header
- Filter dropdown
- Sort by dropdown
- Search plots input field
- Add Plots button
- Export button
- Row checkboxes
- Expandable sidebar sections


5. Colors:
- Primary blue: #3B82F6 (buttons, links)
- Secondary gray: #F3F4F6 (background)
- Text dark: #1F2937
- Badge blue: #EBF5FF
- Border gray: #E5E7EB


6. Grid/Layout Structure:
- Fixed-width sidebar
- Fluid main content
- Table grid: auto columns
- 16px grid spacing
- Responsive container width
</image_analysis>

<development_planning>

1. Project Structure:
```
src/
├── components/
│   ├── layout/
│   │   ├── Header
│   │   ├── Sidebar
│   │   └── MainContent
│   ├── features/
│   │   ├── PlotTable
│   │   ├── FilterControls
│   │   └── StatusBadge
│   └── shared/
├── assets/
├── styles/
├── hooks/
└── utils/
```


2. Key Features:
- Plot listing and filtering
- Status management
- Export functionality
- Plot addition
- Search capabilities
- Entity navigation


3. State Management:
```typescript
interface AppState {
├── plots: {
│   ├── items: Plot[]
│   ├── loading: boolean
│   ├── filters: FilterOptions
│   └── selectedIds: string[]
├── }
├── entities: {
│   ├── activeEntity: string
│   └── expandedSections: string[]
├── }
}
```


4. Routes:
```typescript
const routes = [
├── '/plots',
├── '/plots/:id',
├── '/entities/:id',
└── '/burials/:id'
]
```


5. Component Architecture:
- PlotManagementLayout (parent)
- NavigationSidebar (child)
- PlotListingTable (child)
- FilterControlsBar (child)
- StatusBadgeComponent (shared)


6. Responsive Breakpoints:
```scss
$breakpoints: (
├── 'sm': '640px',
├── 'md': '768px',
├── 'lg': '1024px',
└── 'xl': '1280px'
);
```
</development_planning>